add_library(
    graphs
        graph.h
        graph.cpp
)

include(GenerateExportHeader)

target_include_directories(
    graphs
        PUBLIC ${CMAKE_BINARY_DIR}/exports
        PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
)

generate_export_header(
    graphs
        EXPORT_FILE_NAME ${CMAKE_BINARY_DIR}/exports/graphs_export.h
)

set_target_properties(
    graphs
        PROPERTIES VERSION ${PROJECT_VERSION}
)
