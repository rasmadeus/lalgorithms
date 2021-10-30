add_executable(
    unit_test_graphs
        main.cpp
        graph_test.h
        graph_test.cpp
)

target_link_libraries(unit_test_graphs
    CONAN_PKG::gtest
    graphs
)

add_test(NAME unit_test_graphs COMMAND unit_test_graphs)