# -*- mode: python -*-

block_cipher = None


a = Analysis(['aanda.py'],
             pathex=['C:\\Users\\Daniel.Zwelling\\Documents\\dnd-finder\\dz'],
             binaries=[
               ('C:\\Users\\Daniel.Zwelling\\AppData\\Local\\Programs\\chromedriver_win32\\chromedriver.exe', '.\\selenium\\webdriver')
             ],
             datas=[
               ('C:\\Users\\Daniel.Zwelling\\Documents\\dnd-finder\\dz\\credentials.json', '.'),
               ('C:\\Users\\Daniel.Zwelling\\Documents\\dnd-finder\\dz\\token.json', '.')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='aanda',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='aanda')
