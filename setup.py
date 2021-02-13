from distutils.core import setup, Extension

extra_objects = [
    "ThirdParties/python/lib/libpython3.7m.a",
    "ThirdParties/tbb/lib/libtbb.a",
    "ThirdParties/openexr/lib/libHalf.a",
    "ThirdParties/openvdb/lib/libopenvdb.a",
    "ThirdParties/gmp/lib/libgmp.a",
    "ThirdParties/vcpkg/installed/x64-linux/lib/libz.a",
    "ThirdParties/vcpkg/installed/x64-linux/lib/libgmp.a",
    "ThirdParties/vcpkg/installed/x64-linux/lib/libmpfr.a",
    "ThirdParties/blosc/lib/libblosc.a",
    "ThirdParties/boost/lib/libboost_chrono.a",
    "ThirdParties/boost/lib/libboost_date_time.a",
    "ThirdParties/boost/lib/libboost_filesystem.a",
    "ThirdParties/boost/lib/libboost_iostreams.a",
    "ThirdParties/boost/lib/libboost_locale.a",
    "ThirdParties/boost/lib/libboost_program_options.a",
    "ThirdParties/boost/lib/libboost_regex.a",
    "ThirdParties/boost/lib/libboost_serialization.a",
    "ThirdParties/boost/lib/libboost_system.a",
    "ThirdParties/boost/lib/libboost_thread.a",
    "ThirdParties/boost/lib/libboost_wave.a",
    "ThirdParties/boost/lib/libboost_wserialization.a",
    ]

autoremesher = Extension('autoremesher',
                         define_macros=[
                             ('NDEBUG', None),
                             ('_CRT_SECURE_NO_WARNINGS', None),
                             ('_USE_MATH_DEFINES', None),
                             ('NOMINMAX', None),
                             ('PY_SSIZE_T_CLEAN', None),
                             ('_GLIBCXX_USE_CXX11_ABI', 0)
                             ],
                         undef_macros=['UNICODE', 'AUTOREMESHER_EXPORTS'],
                         include_dirs = [
                             "include/",
                             "ThirdParties/udan_debug/include",
                             "ThirdParties/udan_utils/include",
                             "ThirdParties/geogram/include",
                             "ThirdParties/geogram/geogram_src/src/lib",
                             "ThirdParties/SpdLog/include",
                             "ThirdParties/python3.7/include",
                             "ThirdParties/openvdb/include",
                             "ThirdParties/tbb/include",
                             "ThirdParties/geogram/src/lib",
                             "ThirdParties/geogram",
                             "ThirdParties/libigl/include",
                             "ThirdParties/eigen",
                             "ThirdParties/openexr/include",
                             "ThirdParties/vcpkg/installed/x64-linux/include"
                             ],
                         sources = [
                             'src/pyautoremesher.cpp',
                             "ThirdParties/geogram/geogram_src/src/lib/exploragram/hexdom/basic.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/exploragram/hexdom/frame.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/exploragram/hexdom/polygon.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/exploragram/hexdom/quad_cover.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/exploragram/hexdom/spherical_harmonics_l4.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/algorithm.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/assert.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/attributes.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/b_stream.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/command_line.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/command_line_args.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/common.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/counted.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/environment.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/factory.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/file_system.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/geofile.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/geometry.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/line_stream.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/logger.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/numeric.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/packed_arrays.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/process.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/process_unix.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/process_win.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/progress.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/quaternion.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/stopwatch.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/basic/string.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/bibliography/bibliography.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/bibliography/embedded_references.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/delaunay/delaunay.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/delaunay/delaunay_2d.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/delaunay/delaunay_3d.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/delaunay/delaunay_nn.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/delaunay/delaunay_tetgen.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/delaunay/delaunay_triangle.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/delaunay/LFS.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/delaunay/parallel_delaunay_3d.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/delaunay/periodic.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/delaunay/periodic_delaunay_3d.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/image/colormap.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/image/image.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/image/image_library.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/image/image_rasterizer.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/image/image_serializer.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/image/image_serializer_pgm.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/image/image_serializer_stb.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/image/image_serializer_xpm.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/image/morpho_math.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_AABB.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_baking.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_compare.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_decimate.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_degree3_vertices.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_distance.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_fill_holes.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_frame_field.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_geometry.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_halfedges.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_intersection.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_io.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_manifold_harmonics.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_partition.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_preprocessing.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_remesh.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_reorder.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_repair.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_smoothing.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_subdivision.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_tetrahedralize.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/mesh_topology.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/mesh/triangle_intersection.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_api.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_arpack.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_blas.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_cholmod.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_context.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_cuda.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_iterative_solvers.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_matrix.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_mkl.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_os.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_preconditioners.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/NL/nl_superlu.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/numerics/expansion_nt.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/numerics/lbfgs_optimizers.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/numerics/matrix_util.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/numerics/multi_precision.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/numerics/optimizer.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/numerics/predicates.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/parameterization/mesh_global_param.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/points/co3ne.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/points/colocate.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/points/kd_tree.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/points/nn_search.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/points/principal_axes.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/third_party/LM7/libmeshb7.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/third_party/rply/rply.c",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/voronoi/convex_cell.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/voronoi/CVT.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/voronoi/generic_RVD_cell.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/voronoi/generic_RVD_polygon.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/voronoi/integration_simplex.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/voronoi/RVD.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/voronoi/RVD_callback.cpp",
                             "ThirdParties/geogram/geogram_src/src/lib/geogram/voronoi/RVD_mesh_builder.cpp",
                             "src/autoremesher/autoremesher.cpp",
                             "src/autoremesher/isotropicremesher.cpp",
                             "src/autoremesher/meshseparator.cpp",
                             "src/autoremesher/parameterizer.cpp",
                             "src/autoremesher/positionkey.cpp",
                             "src/autoremesher/quadextractor.cpp",
                             "src/autoremesher/relativeheight.cpp",
                             "src/autoremesher/vdbremesher.cpp",
                             "src/autoremesher/quadmeshgenerator.cpp"
                             ],
                             extra_objects = extra_objects,
                             extra_compile_args=['-std=c++17', '-fpermissive']
                        #  library_dirs=[
                             
                        #      "ThirdParties/zlib/build/Release",
                        #      "ThirdParties/gmp/lib",
                        #      "ThirdParties/vcpkg/installed/x64-windows/lib"
                        #      ],
                        #  libraries=[
                        #      'openvdb',
                        #      'udan_debug',
                        #      'geogram',
                        #      "libgmp-10",
                        #      "Half_s",
                        #      "zlib"
                        #      ]

                        
                         )

setup(
    name        = 'autoremesher',
    version     = '1.0',
    description = 'Sample python C-API exploration',
    ext_modules = [autoremesher]
)
