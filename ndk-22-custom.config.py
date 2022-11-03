COMMON_CMAKE_VAR = dict(
                OPENCV_DISABLE_FILESYSTEM_SUPPORT='ON',
                WITH_ITT='OFF',
                BUILD_FAT_JAVA_LIB='ON',
                WITH_OPENJPEG='OFF',
                WITH_OPENEXR='OFF',
                WITH_JASPER='OFF',
                WITH_JPEG='OFF',
                packbits='OFF',
                WITH_PROTOBUF='OFF',
                mdi='OFF')

ABIs = [
    ABI("2", "armeabi-v7a", None, cmake_vars=dict(ENABLE_NEON='ON', ANDROID_ABI='armeabi-v7a with NEON', ANDROID_GRADLE_PLUGIN_VERSION='7.2.0', GRADLE_VERSION='7.5', KOTLIN_PLUGIN_VERSION='1.5.10')),
    ABI("3", "arm64-v8a",   None, cmake_vars=dict(ENABLE_NEON='ON', ANDROID_GRADLE_PLUGIN_VERSION='7.2.0', GRADLE_VERSION='7.5', KOTLIN_PLUGIN_VERSION='1.5.10')),
    ABI("5", "x86_64",      None, cmake_vars=dict(ANDROID_GRADLE_PLUGIN_VERSION='7.2.0', GRADLE_VERSION='7.5', KOTLIN_PLUGIN_VERSION='1.5.10')),
    ABI("4", "x86",         None, cmake_vars=dict(ANDROID_GRADLE_PLUGIN_VERSION='7.2.0', GRADLE_VERSION='7.5', KOTLIN_PLUGIN_VERSION='1.5.10')),
]

for i, abi in enumerate(ABIs):
    abi.cmake_vars.update(COMMON_CMAKE_VAR)
