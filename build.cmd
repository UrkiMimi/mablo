python -m nuitka ^
--onefile ^
--disable-console ^
--windows-icon-from-ico=mablo.ico ^
--enable-plugin=tk-inter ^
--follow-imports ^
--product-name="mablo" ^
--product-version="0.2.1" main.py