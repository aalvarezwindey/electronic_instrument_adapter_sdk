# Contributing

## Make your changes

Make your changes in the SDK: `/electronic_instrument_adapter_sdk`

Update `setup.py` if necessary:
1. Add external packages to `intal_requires` property. Only for no standard Python packages.
2. Update classifiers if applies (development status and Python version).

## Publish a new version

After commiting your changes run the script `./create_release.py`. This will:
1. List repository tags.
2. Request you to enter a new version for the SDK.
3. Generates the new `setup.py` file (with the version provided).
4. Commit that change and generate git tag.
5. Push tag to current branch

After that, the CI with GitHub action will build and publish the new version according to the steps provided in `.github/workflows/main.yml`
