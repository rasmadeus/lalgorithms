add_library(
    graphs
        union_find.h
        union_find.cpp
)

include(GenerateExportHeader)
generate_export_header(
    graphs
        EXPORT_FILE_NAME ${CMAKE_BINARY_DIR}/exports/graphs_export.h
)

target_include_directories(
    graphs
        PUBLIC ${CMAKE_BINARY_DIR}/exports
        PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
)

set_target_properties(
    graphs
        PROPERTIES VERSION ${PROJECT_VERSION}
)
