
<H1>Installation</H1>

```
#setup path for RapidEtl project
RAPIDETLPATH=/path/to/your/project/rapidEtl-0.0.0

#for now using libs from venv/
RAPIDETLLIBSPATH=$RAPIDETLPATH/venv/lib/python3.6/site-packages/:$RAPIDETLPATH/venv/share

export PYTHONPATH=$PYTHONPATH:$RAPIDETLPATH:$RAPIDETLLIBSPATH

```

need to figure out how to automaticly get this binary into common/reources:
https://drive.google.com/drive/folders/1L8ni2IIagJZerj8z2oQT1rNbSHRgqtur?usp=sharing
