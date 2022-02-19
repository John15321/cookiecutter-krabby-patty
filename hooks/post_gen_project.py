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
    basedir = os.path.dirname(PROJECT_DIRECTORY)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    with open(filepath, "w") as f:
        f.write(content)


if __name__ == "__main__":
    if "{{ cookiecutter.crate_type }}" == "bin":
        create_file("./src/main.rs", MAIN_RS_CONTENT)
    elif "{{ cookiecutter.crate_type }}" == "lib":
        create_file("./src/lib.rs", LIB_RS_CONTENT)
