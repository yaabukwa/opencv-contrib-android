COMMON_CMAKE_VAR = dict(
                CMAKE_BUILD_TYPE='Release',
                CMAKE_CONFIGURATION_TYPES='Release',
                CMAKE_CXX_FLAGS='-O3',
                CMAKE_C_FLAGS='-O3',
                OPENCV_DISABLE_FILESYSTEM_SUPPORT='ON',
                WITH_ITT='OFF',
                WITH_TBB='ON',
                BUILD_TBB='ON',
                BUILD_FAT_JAVA_LIB='ON',
                WITH_EIGEN='ON',
                WITH_OPENJPEG='OFF',
                WITH_OPENEXR='OFF',
                WITH_JASPER='OFF',
                WITH_JPEG='OFF',
                packbits='OFF',
                WITH_PROTOBUF='OFF',
                mdi='OFF')

ABIs = [
    ABI("2", "armeabi-v7a", None, cmake_vars=dict(ENABLE_THIN_LTO='ON', ENABLE_NEON='ON', ENABLE_VFPV3='ON', ENABLE_THIN_LTO='ON', ANDROID_ABI='armeabi-v7a with NEON', ANDROID_GRADLE_PLUGIN_VERSION='7.2.0', GRADLE_VERSION='7.5', KOTLIN_PLUGIN_VERSION='1.5.10')),
    ABI("3", "arm64-v8a",   None, cmake_vars=dict(ENABLE_THIN_LTO='ON', ENABLE_NEON='ON', ENABLE_VFPV3='ON', ENABLE_THIN_LTO='ON', ANDROID_GRADLE_PLUGIN_VERSION='7.2.0', GRADLE_VERSION='7.5', KOTLIN_PLUGIN_VERSION='1.5.10')),
    ABI("5", "x86_64",      None, cmake_vars=dict(ENABLE_LTO='ON', ANDROID_GRADLE_PLUGIN_VERSION='7.2.0', GRADLE_VERSION='7.5', KOTLIN_PLUGIN_VERSION='1.5.10')),
    ABI("4", "x86",         None, cmake_vars=dict(ENABLE_LTO='ON', ANDROID_GRADLE_PLUGIN_VERSION='7.2.0', GRADLE_VERSION='7.5', KOTLIN_PLUGIN_VERSION='1.5.10')),
]

for i, abi in enumerate(ABIs):
    abi.cmake_vars.update(COMMON_CMAKE_VAR)
