
import argparse
import pandas as pd
from pathlib import Path

import wcsimreader.utils as wcr


list_keys = [
                # "wcsimGeoT/Geometry",
                "wcsimGeoT/PMT",
                "wcsimRootOptionsT",
                "wcsimT/CherenkovHitTimes",
                "wcsimT/CherenkovHits",
                "wcsimT/Tracks",
                "wcsimT/Triggers"
             ]

def main():

    parser = argparse.ArgumentParser( prog        = "wcsim_hdf5_to_csv"
                                    , description = "Converts WCSim .h5 files into .csv"
                                    , epilog      = "Text at the bottom of help")


    parser.add_argument( "infile", type=str, help = ".h5 files")
    parser.add_argument( "-o", "--outpath", type=str, nargs="?", help = ".csv file path", default=".")


    args = parser.parse_args()

    convert(args.infile, args.outpath)

def convert(infile, outpath):
    """
    Converts hdf5 file into several csv files.
    It utilizes the wcsimreader.utils.read_table function to extract the proper informations.
    For the /wcsimGeoT/Geometry group, since there are only the radius, length and PMT radius, the informations are
    manually saved into a csv files with labels.
    """
    wcr.explore_file(infile)

    # Handle geometry
    # This is a rather odd thing, so we do it manually
    print(f"Reading /wcsimGeoT/Geometry or Settings")
    geometry = wcr.read_table(infile, "/wcsimGeoT/Geometry")
    radius = geometry["WCCylRadius"][0]
    length = geometry["WCCylLength"][0]
    pmt_radius = geometry["WCPMTRadius"][0]

    try:
        settings = wcr.read_table(infile, "Settings")
        radius = settings["WCDetRadius"][0] * 0.1
        length = settings["WCDetHeight"][0] * 0.1
    except LookupError:
        pass

    csv_file_name = f"{Path(infile).stem}_wcsimGeoT/Geometry.csv".replace("/", "_")
    csv_file_path = f"{outpath}/{csv_file_name}"

    print(f"Writing to {csv_file_path}")
    with open(csv_file_path, 'w') as file:
        file.write(f'Radius,{radius}\n')
        file.write(f'Length,{length}\n')
        file.write(f'PMTRadius,{pmt_radius}\n')

    # Handle all the other groups
    for key in list_keys:
        print(f"Reading key {key}")
        df = wcr.read_table(infile, key)
        csv_file_name = f"{Path(infile).stem}_{key}.csv".replace("/", "_")
        csv_file_path = f"{outpath}/{csv_file_name}"
        print(f"Writing to {csv_file_path}")
        df.to_csv(csv_file_path, index=False)
        print(f'Table {key} saved to {csv_file_path}')
    return True

if __name__ == "__main__":
    main()