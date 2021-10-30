#pragma once

#include <gtest/gtest.h>
#include <union_find.h>

class UnionFindTest : public testing::Test
{
protected:
    void SetUp() override;

protected:
    lalg::UnionFind m_graph{ 1 };
};
