# Data Legislation

This repository is a collection of interviews that enable the user to determine the consequences of various EU data legislations. This is created as part of the docassemble application. The interviews are created in YAML format and are uploaded on Docassemble instance as python packages.

## Steps for creating new interviews
1. Create a new branch for each interview (like database_directive, privacy, whistleblowing etc.)
2. In the root of repo, these files are necessary - `setup.py`, `setup.cfg`, and `MANIFEST.in`
3. The files can be copied from any other existing branch using `git checkout database_directive setup.cfg setup.py MANIFEST.in` in the root of the repository in the new branch.
4. Under `docassemble` directory, create the directory (name of your choice). Similarly, under the new subdirectory, create directories `data/questions`. You can do so on the command line using `mkdir -p docassemble/<directory name of your choice>/data/questions` from the root of the repo.
5. Navigate to the `docassemble` directory using `cd docassemble` from the root of the repo, and perfom `git checkout database_directive Database_directive/__init__.py`
6. Move `__init__.py` by doing `mv Database_directive/__init__.py <directory name of your choice>/` from the location of `docassemble` directory.
7. Remove `Database_directive` by doing `rmdir Database_directive` from the `docassemble` directory.
8. Within `docassemble` directory, perform `git checkout database_directive __init__.py`
10. Navigate back to the root of the repo and edit the following parts in the file `setup.py` and method `setup` -
 - `name` value with a name of your liking like so `docassemble.<your new name>`
 - `long_description` value with your description
 - `package_data` parameters `where` with value `docassemble/<your new directory name>` and `package` value with `docassemble.<your new name>`
11. There are two files required in data/questions. You can place your actual interview file with questions in `<your file name>.yml` and `interview.yml`file that basically indicates to include relevant files. You can check other branches as example.
12. Save the modified information and do `git push`

## Steps for uploading on Docassemble instance
1. Navigate to `Playground`
2. Provide a unique package name (it is case sensitive)
3. Under `Folder`-> Click on `Package` -> Click on `Pull` -> Provide `Github repo URL` -> Select `<Your new branch>`
4. Install


## Alternative
Visit docassemble page for how to upload interviews through PDF or DOCX documents

`P.S. Package names are case sensitive`
