#pragma once

#include <gtest/gtest.h>
#include <graph.h>

class GraphTest : public testing::Test
{
protected:
    void SetUp() override;

protected:
    lalg::Graph m_graph;
};
