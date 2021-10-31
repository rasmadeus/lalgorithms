#pragma once

#include <gtest/gtest.h>
#include <union_find.h>

namespace lalg
{
    class UnionFindTest : public testing::Test
    {
    protected:
        lalg::UnionFind m_unionFind{ 10 };
    };
}
