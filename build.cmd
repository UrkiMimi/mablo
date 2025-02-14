python -m nuitka ^
--onefile ^
--windows-icon-from-ico=mablo.ico ^
--enable-plugin=tk-inter ^
--follow-imports ^
--product-name="mablo" ^
--disable-console ^
--product-version="0.2.1" main.py

del mablo.mbo
ren main.exe mablo.mbo