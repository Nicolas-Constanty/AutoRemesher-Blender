copy bin\Release\autoremesher.pyd mesh_autoremesher\src
powershell -Command "Compress-Archive -LiteralPath 'mesh_autoremesher\'  -DestinationPath mesh_autoremesher.zip"