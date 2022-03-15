#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

MAIN_RS_CONTENT = r"""fn main() {
    println!("Hello, world!");
}
"""

LIB_RS_CONTENT = r"""#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
"""


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def create_file(filepath, content):
    basedir = os.path.dirname(filepath)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    with open(filepath, "w") as f:
        f.write(content)


def delete_github_ci():
    pass


def delete_gitlab_ci():
    pass


def delete_jenkins_ci():
    pass


def readme_toc_update() -> None:
    """Checks and updates toc in readme.md.

    Creates temp.txt file to store temporary data

    Returns
    -------
    None
    """
    with open("../{{ cookiecutter.project_short_name }}/README.md", "r") as file_read:
        with open("./temp.txt", "w") as temp_write:
            temp_write.write("\n")
            temp_write.write("<!TOC_START>\n\n")
            lines = file_read.readlines()
            for line in lines:
                if line.startswith("## ") and not line.startswith(
                    "## Table of Contents"
                ):
                    text = line[3:-2]
                    readme_toc_syntax = text.lower().replace(" ", "-")
                    temp_write.write(f"* [{text}]({readme_toc_syntax})")
                    temp_write.write("\n\n")

                if line.startswith("### "):
                    text = line[4:-1]
                    readme_toc_syntax = text.lower().replace(" ", "-")
                    temp_write.write(f"  * [{text}]({readme_toc_syntax})")
                    temp_write.write("\n\n")
            temp_write.write("<!TOC_END>")

        with open(
            "../{{ cookiecutter.project_short_name }}/README.md", "a"
        ) as file_write:
            with open("./temp.txt", "r") as temp_read:
                start_index = 0
                end_index = 0
                for num, line in enumerate(lines):
                    if line.startswith("<!TOC_START"):
                        start_index = num
                    if line.startswith("<!TOC_END>"):
                        end_index = num + 1
                file_write.truncate(0)
                file_write.seek(0)
                for num, line in enumerate(lines):
                    if num not in [index for index in range(start_index, end_index)]:
                        file_write.write(line)
                    if line.startswith("## Table of Contents"):
                        file_write.writelines(temp_read.readlines())


def delete_all_ci_configurations():
    delete_github_ci()
    delete_gitlab_ci()
    delete_jenkins_ci()


if __name__ == "__main__":
    # Create basic source file in src/
    if "{{ cookiecutter.crate_type }}" == "bin":
        create_file("./src/main.rs", MAIN_RS_CONTENT)
    elif "{{ cookiecutter.crate_type }}" == "lib":
        create_file("./src/lib.rs", LIB_RS_CONTENT)

    # Delete unwanted CI/CD pipeline configurations
    if "{{ cookiecutter.ci_configuration }}" == "GitHub Actions":
        delete_gitlab_ci()
        delete_jenkins_ci()
    elif "{{ cookiecutter.ci_configuration }}" == "GitLab":
        delete_github_ci()
        delete_jenkins_ci()
    elif "{{ cookiecutter.ci_configuration }}" == "Jenkins":
        delete_github_ci()
        delete_gitlab_ci()
    elif "{{ cookiecutter.ci_configuration }}" == "None":
        delete_all_ci_configurations()

    # If the project is not Open Source delete the LICENSE file
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    # Initialize the git repository
    if "{{ cookiecutter.default_git_branch }}" != "None":
        os.system("git init -b {{ cookiecutter.default_git_branch }}")
