from conans import ConanFile, CMake, tools


class OscpackConan(ConanFile):
    name = "oscpack"
    version = "1.1.0"
    license = "MIT"
    url = "https://github.com/czoido/conan-oscpack"
    homepage = "https://code.google.com/archive/p/oscpack"
    description = "Oscpack is simply a set of C++ classes for packing and unpacking OSC packets"
    topics = ("osc", "midi", "music")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    _source_subfolder = "oscpack_1_1_0"
    _build_subfolder = "build"

    def source(self):
        tools.get(**self.conan_data["sources"]["1.1.0"])

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy("*.h", dst="include/osc", src="{}/osc".format(self._source_subfolder))
        self.copy("*.h", dst="include/ip", src="{}/ip".format(self._source_subfolder))
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["oscpack"]
        if self.settings.os == "Windows":
            self.cpp_info.libs.extend(["Ws2_32", "winmm"])

