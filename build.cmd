python -m nuitka ^
--onefile ^
--windows-icon-from-ico=mablo.ico ^
--enable-plugin=tk-inter ^
--disable-console ^
--follow-imports ^
--product-name="mablo" ^
--product-version="0.2.1" main.py