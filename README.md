# Container Action Template

Validates branch name according to pr_lint.json configuration file in the calling repository.  
This can be used in as an automated workflow to check pull request branch validation, as seen [here](https://github.com/wirecard/woocommerce-ee/blob/master/.github/workflows/pr_lint.yml)

## How to setup

Simply add the action to your workflow
````
- name: Validate PR branch name
    uses: wirecard/pr-lint@master
    with:
      branch: <branch_name>
````
And adapt ````pr_lint.json```` to your repositories.  
Below you can find an [example configuration](#example-pr_lintjson). 

## How to configure

The script takes the regex out of the ````pr_lint.json````.

## Example pr_lint.json

### Mandatory example pr_lint.json
````json
{
	"pattern": "^(RC-(([0-9])+\\.){2}([0-9])+-(patch|minor|major))$|-(test|documentation|feature|configuration|force)$|^(dependabot)"
}
````

## Short overview of the file structure

### main.py

The ```main.py``` file is the main file called through ```entrypoint.sh``` in the container.  
It calls the required objects in the correct order and executes the necessary methods.
