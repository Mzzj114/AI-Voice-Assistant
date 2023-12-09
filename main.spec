# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py','audioReco.py','tts.py','yiyanAPI.py'],
    pathex=['D:\\User\\document\\program\\_Py\\AI_helper'],
    binaries=[],
    datas=[('D:\\User\\document\\program\\_Py\\AI_helper\\model\\*','model')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AIhelper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    icon='D:\\User\\document\\program\\_Py\\AI_helper\\superhero_icon.ico',
    codesign_identity=None,
    entitlements_file=None,
)
