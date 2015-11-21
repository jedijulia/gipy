gitignorepy
===========

generates `.gitinore` files using templates from [gitignore.io](https://gitignore.io)


#### Usage

```
$ gitignorepy [options] <space-separated names of languages/frameworks>
# e.g. gitignorepy python django
```

By default, this will just print out the generated contents on the terminal

#### Options

`-w`, `--write`: write the generated contents to a file named `.gitignore`
