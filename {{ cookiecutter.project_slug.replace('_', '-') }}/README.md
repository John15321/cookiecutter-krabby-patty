[![semantic-release](https://img.shields.io/badge/semantic--release-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

# {{ cookiecutter.project_full_name }}

{{ cookiecutter.project_short_description }}

## Contributing and Releasing

---

The repository follows a semantic release development and release cycle.
This means that all PRs merged into `main`/`master` need to have formats like these:

- `feat(ABC-123): Adds /get api response`
- `fix(MINOR): Fix typo in the CI`
- `fix(#12345): Fix memory leak`
- `ci(Just about anything here): Update Python versions in the CI`

Here is the exact enforced regular expression:

```regex
'^(fix|feat|docs|test|perf|ci|chore)\([^)]+\): .+'
```

Allowed types of conventional commits:

- `fix`: a commit that fixes a bug.
- `feat`: a commit that adds new functionality.
- `docs`: a commit that adds or improves documentation.
- `test`: a commit that adds unit tests.
- `perf`: a commit that improves performance, without functional changes.
- `ci`: a commit that adds or improves the CI configuration.
- `chore`: a catch-all type for any other commits. For instance, if you're implementing a single feature and it makes sense to divide the work into multiple commits, you should mark one commit as feat and the rest as chore.

Releasing the package is done automatically when a commit is merged to `main`/`master`. A new release is created and the `CHANGELOG.md` is updated automatically.

More about the releasing mechanism:
<https://github.com/semantic-release/semantic-release>

## Credits

This package was created with Cookiecutter, and the
`John15321/cookiecutter-krabby-patty` project template.

Cookiecutter: <https://github.com/audreyr/cookiecutter>

`John15321/cookiecutter-krabby-patty`: <https://github.com/John15321/cookiecutter-krabby-patty>
