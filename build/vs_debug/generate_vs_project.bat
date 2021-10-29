set PRO_ROOT=%~dp0/../..
set BUILD_TYPE=Debug

conan install %PRO_ROOT% --profile %~dp0/conan_debug_profile
cmake -G "Visual Studio 16 2019" -DCMAKE_BUILD_TYPE=%BUILD_TYPE% %PRO_ROOT%
cmake --build .