# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['UVR.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('gui_data', '.'),
        ('models', '.'),
        ('ffmpeg.exe', '.'),
        ('ffplay.exe', '.'),
        ('ffprobe.exe', '.'),
        ('rubberband-r3.exe', '.'),
        ('rubberband.exe', '.'),
        ('sndfile.dll', '.'),
    ],
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
    [],
    exclude_binaries=True,
    name='UVR',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['gui_data\\img\\GUI-Icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='UVR',
)
