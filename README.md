<img src="./img/krabby_patty.png"  width=25% height=25%>

You need to install cookiecutter to use it:

```bash
pip install cookiecutter
```

Usage:
```bash
$ cookiecutter https://github.com/John15321/cookiecutter-krabby-patty
```

This template configures:
* CI jobs for
 * Formatting check
 * Linting check
 * Builds on `ubuntu`, `macos`, `ubuntu` each with `stable`, `beta`, `nightly`, `toolchains`
 * Tests on `ubuntu`, `macos`, `ubuntu` each with `stable`, `beta`, `nightly`, `toolchains`
 * Checking package integrity and pubirsh dry-run
 * `Makefile.toml` using [cargo-make](https://crates.io/crates/cargo-make)
 * Choose a license
 * README badges
 * Dependency license check using [cargo-deny](https://crates.io/crates/cargo-deny)
 * Dependency vulnurabilities audit using [cargo-audit](https://crates.io/crates/cargo-audit)
