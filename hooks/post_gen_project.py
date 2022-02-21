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
