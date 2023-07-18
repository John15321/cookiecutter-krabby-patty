const config = {
  branches: ['main', 'master'],

  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    [
      "@semantic-release/exec",
      {
        "prepareCmd": "echo ${nextRelease.version} > .VERSION ; cargo install cargo-bump ; cargo bump $(cat .VERSION | sed 's/^[a-zA-Z]*//') ; cargo package --allow-dirty"
      }
    ],
    [
      "@semantic-release/github",
      {
        "assets": [
          { "path": "target/package/*" },
        ]
      }
    ],
    [
      "@semantic-release/changelog",
      {
        "changelogFile": "CHANGELOG.md"
      }
    ],
    [
      "@semantic-release/git",
      {
        "assets": ["CHANGELOG.md", "Cargo.toml", "Cargo.lock"],
        "message": "chore(Release 🚀): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}",
      }
    ]
  ],
};
module.exports = config;
