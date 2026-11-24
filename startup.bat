echo off

SET OSGEO4W_ROOT=C:\OSGeo4W
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
path %PATH%;%OSGEO4W_ROOT%\apps\Python312\Scripts
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python
set PYTHONHOME=%OSGEO4W_ROOT%\apps\Python312

rem SET OSGEO4W_ROOT=C:\OSGeo4W
rem call C:\OSGeo4W\bin\o4w_env.bat
rem path %PATH%;C:\OSGeo4W\apps\qgis\bin
rem path %PATH%;C:\OSGeo4W\apps\Python312\Scripts
rem set PYTHONPATH=%PYTHONPATH%;C:\OSGeo4W\apps\qgis\python
rem set PYTHONHOME=C:\OSGeo4W\apps\Python312

start /d "C:\Program Files\Microsoft VS Code\" Code.exe