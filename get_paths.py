from pandas import read_csv
from argparse import ArgumentParser

def get_paths(samples_file, assemblies_dir, scaffolds_dir):
    """Produce file paths of assembly and scaffold files"""
    ids_df = read_csv(samples_file)

    assembly_paths = [glob.glob(assemblies_dir + sample) for sample in ids_df.iloc[:, 0]]
    scaffold_paths = [glob.glob(scaffolds_dir + sample) for sample in ids_df.iloc[:, 1]]

    return assembly_paths, scaffold_paths


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--samples_file")
    parser.add_argument("--assemblies_dir")
    parser.add_argument("--scaffolds_dir")
    args = parser.parse_args()

    assembly_paths, scaffold_paths = get_paths(args.samples_file, args.assemblies_dir, args.scaffolds_dir)
    print(assembly_paths, scaffold_paths)