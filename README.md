### tap-oracle

Tap for Oracle

you must enable supplemental logging before turning on logminer
 begin
 rdsadmin.rdsadmin_util.alter_supplemental_logging(
   p_action => 'ADD');
 end;


begin
    rdsadmin.rdsadmin_util.set_configuration(
        name  => 'archivelog retention hours',
        value => '24');
end;

QL> exec rdsadmin.rdsadmin_util.show_configuration;
NAME:tracefile retention
VALUE:10080
DESCRIPTION:tracefile expiration specifies the duration in minutes before
tracefiles in bdump are automatically deleted.
NAME:archivelog retention hours
VALUE:24
DESCRIPTION:ArchiveLog expiration specifies the duration in hours before
archive/redo log files are automatically deleted.
/

---

Copyright &copy; 2018 Stitch

### Install and Run

Ensure poetry is installed on your machine. 

- This command will return the installed version of poetry if it is installed.
```
poetry --version
```

- If not, install poetry using the following commands (from https://python-poetry.org/docs/#installation):
```
curl -sSL https://install.python-poetry.org | python3 -
PATH=~/.local/bin:$PATH
```

Within the `tap-oracle` directory, install dependencies:
```
poetry install
```

Then run the tap:
```
poetry run tap-oracle <options>
```

## Create a Config file

## Run Discovery

```
> tap-oracle --config config.json --discover > properties.json
```

## Sync Data

```
> tap-oracle --config config.json --properties properties.json
```