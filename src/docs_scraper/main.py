import glob

def replace_exact(docs_dir, exact_str, replace_str):
    all_md_files = glob.glob(f"{docs_dir}**/*.md", recursive=True)

    for file in all_md_files:
        file_content = [line for line in open(file, encoding="utf8")]
        writer = open(file, 'w', encoding="utf8")

        for line in file_content:
            # We search for the correct section
            section = False
            if exact_str in line:
                section = True

            # Once we arrive at the correct position, write the new entry
            if section == True:
                writer.write(line.replace(exact_str, replace_str))
                continue
            writer.write(line)

        writer.close()


def find_exact (docs_dir, exact_str):
    all_md_files = glob.glob(f"{docs_dir}**/*.md", recursive=True)

    index_file_list = []
    for file in all_md_files:
        file_content = [line for line in open(file, encoding="utf8")]

        index_list = []
        for i, line in enumerate(file_content):
            # We search for the correct section
            section = False
            if exact_str in line:
                index_list.append(i)

        index_file_list.append({file:index_list})

    return index_file_list



