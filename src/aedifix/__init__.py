# SPDX-FileCopyrightText: Copyright (c) 2021-2025 NVIDIA CORPORATION & AFFILIATES.
#                         All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from . import cmake, package, packages, util
from ._version import version as __version__
from .cmake import (
    CMAKE_VARIABLE,
    CMakeBool,
    CMakeExecutable,
    CMakeInt,
    CMakeList,
    CMakePath,
    CMaker,
    CMakeString,
)
from .main import basic_configure
from .manager import ConfigurationManager
from .package import MainPackage, Package
from .util.argument_parser import ArgSpec, ConfigArgument

__all__ = (
    "CMAKE_VARIABLE",
    "ArgSpec",
    "CMakeBool",
    "CMakeExecutable",
    "CMakeInt",
    "CMakeList",
    "CMakePath",
    "CMakeString",
    "CMaker",
    "ConfigArgument",
    "ConfigurationManager",
    "MainPackage",
    "Package",
    "__version__",
    "basic_configure",
    "cmake",
    "package",
    "packages",
    "util",
)
