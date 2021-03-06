# -*- coding: utf-8 -*-
'''Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2016, Caleb Bell <Caleb.Andrew.Bell@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''

from __future__ import division
from fluids import *
from numpy.testing import assert_allclose
import pytest

def test_friction():
    assert_allclose(Moody(1E5, 1E-4), 0.01809185666808665)
    assert_allclose(Alshul_1952(1E5, 1E-4), 0.018382997825686878)
    assert_allclose(Wood_1966(1E5, 1E-4), 0.021587570560090762)
    assert_allclose(Churchill_1973(1E5, 1E-4), 0.01846708694482294)
    assert_allclose(Eck_1973(1E5, 1E-4), 0.01775666973488564)
    assert_allclose(Jain_1976(1E5, 1E-4), 0.018436560312693327)
    assert_allclose(Swamee_Jain_1976(1E5, 1E-4), 0.018452424431901808)
    assert_allclose(Churchill_1977(1E5, 1E-4), 0.018462624566280075)
    assert_allclose(Chen_1979(1E5, 1E-4), 0.018552817507472126)
    assert_allclose(Round_1980(1E5, 1E-4), 0.01831475391244354)
    assert_allclose(Shacham_1980(1E5, 1E-4), 0.01860641215097828)
    assert_allclose(Barr_1981(1E5, 1E-4), 0.01849836032779929)
    assert_allclose(Zigrang_Sylvester_1(1E5, 1E-4), 0.018646892425980794)
    assert_allclose(Zigrang_Sylvester_2(1E5, 1E-4), 0.01850021312358548)
    assert_allclose(Haaland(1E5, 1E-4), 0.018265053014793857)
    assert_allclose(Serghides_1(1E5, 1E-4), 0.01851358983180063)
    assert_allclose(Serghides_2(1E5, 1E-4), 0.018486377560664482)
    assert_allclose(Tsal_1989(1E5, 1E-4), 0.018382997825686878)
    assert_allclose(Tsal_1989(1E8, 1E-4), 0.012165854627780102)
    assert_allclose(Manadilli_1997(1E5, 1E-4), 0.01856964649724108)
    assert_allclose(Romeo_2002(1E5, 1E-4), 0.018530291219676177)
    assert_allclose(Sonnad_Goudar_2006(1E5, 1E-4), 0.0185971269898162)
    assert_allclose(Rao_Kumar_2007(1E5, 1E-4), 0.01197759334600925)
    assert_allclose(Buzzelli_2008(1E5, 1E-4), 0.018513948401365277)
    assert_allclose(Avci_Karagoz_2009(1E5, 1E-4), 0.01857058061066499)
    assert_allclose(Papaevangelo_2010(1E5, 1E-4), 0.015685600818488177)
    assert_allclose(Brkic_2011_1(1E5, 1E-4), 0.01812455874141297)
    assert_allclose(Brkic_2011_2(1E5, 1E-4), 0.018619745410688716)
    assert_allclose(Fang_2011(1E5, 1E-4), 0.018481390682985432)

    assert_allclose(sum(_roughness.values()), 0.01504508)

    assert_allclose(friction_factor(Re=1E5, eD=1E-4), 0.018513866077471648)
    methods_1 = friction_factor(Re=1E5, eD=1E-4, AvailableMethods=True)
    methods_1.sort()

    methods_2 = ['Manadilli_1997', 'Haaland', 'Alshul_1952', 'Avci_Karagoz_2009', 'Rao_Kumar_2007', 'Zigrang_Sylvester_2', 'Eck_1973', 'Buzzelli_2008', 'Tsal_1989', 'Papaevangelo_2010', 'Barr_1981', 'Jain_1976', 'Moody', 'Brkic_2011_2', 'Brkic_2011_1', 'Swamee_Jain_1976', 'Wood_1966', 'Shacham_1980', 'Romeo_2002', 'Chen_1979', 'Fang_2011', 'Round_1980', 'Sonnad_Goudar_2006', 'Churchill_1973', 'Churchill_1977', 'Serghides_2', 'Serghides_1', 'Zigrang_Sylvester_1']
    methods_2.sort()
    assert methods_1 == methods_2

    assert_allclose(friction_factor(Re=1E5, eD=1E-4, Darcy=False), 0.018513866077471648*4)
