# Plist Image Extractor

**Requirement: python, PILLOW not PIL (because of transparent problems)**

## How to use

Has to have a png file and a plist file with same name in same dir.
ex:

tiles.plist
tiles.png

```
python plistExtractor.py tiles
```
Or if you don't pass file name, you can extract all plist file in the same dir

```
python plistExtractor.py
```

## Warning

Different tools will generate different format plist, make sure your plist like below, or you can modify code to make it compatible

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>frames</key>
        <dict>
            <key>bkg.png</key>
            <dict>
                <key>aliases</key>
                <array/>
                <key>spriteOffset</key>
                <string>{0,0}</string>
                <key>spriteSize</key>
                <string>{240,400}</string>
                <key>spriteSourceSize</key>
                <string>{240,400}</string>
                <key>textureRect</key>
                <string>{{1,1},{240,400}}</string>
                <key>textureRotated</key>
                <true/>
            </dict>
        </dict>
    </dict>
</plist>
```
