#pragma once

#include <gtest/gtest.h>
#include <union_find.h>

namespace lalg
{
    class UnionFindTest : public testing::Test
    {
    protected:
        lalg::QuickFind m_quickFind{ 10 };
        lalg::QuickUnion m_quickUnion{ 10 };
    };
}
