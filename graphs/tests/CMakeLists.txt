add_executable(
    unit_test_graphs
        main.cpp
        union_find_test.h
        union_find_test.cpp
)

target_link_libraries(unit_test_graphs
    CONAN_PKG::gtest
    graphs
)

add_test(NAME unit_test_graphs COMMAND unit_test_graphs)