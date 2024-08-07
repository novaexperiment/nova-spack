diff --git a/CMakeLists.txt b/CMakeLists.txt
index ca8c16a..a30e454 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -1,10 +1,13 @@
-cmake_minimum_required(VERSION 3.10)
+cmake_minimum_required(VERSION 3.20 FATAL_ERROR)
 
 ############   top level config
 
-project(NOvARwgt)
-set(VERSION "v3.0-dev6")
+find_package(cetmodules REQUIRED)
+project(novarwgt VERSION 3.0.6 LANGUAGES CXX C)
 
+include(CetCMakeEnv)
+cet_cmake_env()
+
 set(CMAKE_CXX_STANDARD 17)
 set(CMAKE_SKIP_RPATH false)
 
@@ -19,8 +22,6 @@ set(CMAKE_CXX_FLAGS_MINSIZEREL "${common_flags} -Os")
 set(CMAKE_CXX_FLAGS_RELEASE "${common_flags} -O2")
 set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${common_flags} -g -O2")
 
-list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake/Modules")
-
 # the BUILD_TYPE and UPS_... vars are only used when working with UPS,
 # but that means they're needed in the FindCET.cmake called by some of the external dependencies
 if (${CMAKE_BUILD_TYPE} MATCHES "Debug")
@@ -81,13 +82,13 @@ set(NOVARWGT_ROOT_LIBRARIES ${ROOT_LIBRARIES})
 # Fermi products which are often useful
 option(NOVARWGT_USE_CETLIB "Use FNAL CETLib?" Off)
 if(NOVARWGT_USE_CETLIB)
-	find_package(CETLib)
+	find_package(cetlib)
 endif()
 
 # GENIE
 option(NOVARWGT_USE_GENIE "Build support for GENIE?" On)
 if(NOVARWGT_USE_GENIE)
-	find_package(GENIE)
+	find_package(genie)
 else()
 	set(NOVARWGT_GENIE_QUAL "nogenie")
 endif()
@@ -95,7 +96,7 @@ endif()
 # FNAL NuSimData
 option(NOVARWGT_USE_NUSIMDATA "Build support for FNAL NuSimData?" On)
 if(NOVARWGT_USE_NUSIMDATA)
-	find_package(NuSimData)
+	find_package(nusimdata)
 endif()
 
 ###########   source can be installed with build if user desires
