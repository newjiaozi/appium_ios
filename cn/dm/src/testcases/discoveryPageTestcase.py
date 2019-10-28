#coding=utf-8

from .baseTestcase import BaseTestcase
import unittest

class DiscoveryPageTestcase(BaseTestcase):


    # @unittest.skip("无条件跳过该测试")
    def test001_checkDefaultHotWord(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkDefaultHotWord())

    # @unittest.skip("无条件跳过该测试")
    def test003_checkSearchPage(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInSearchInput())
        self.assertTrue(self.DPA.checkGenreUI())
        self.assertTrue(self.DPA.checkDefaultSearchUI())

    # @unittest.skip("无条件跳过该测试")
    def test004_checkSearchBtn(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInSearchBtn())
        self.assertTrue(self.DPA.checkSearchBtn())

    # @unittest.skip("无条件跳过该测试")
    def test005_checkBigbanner(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkBigBanner())

    # @unittest.skip("无条件跳过该测试")
    def test006_checkGenrePage(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInGenre())
        self.assertTrue(self.DPA.checkGenrePage())
        self.assertTrue(self.DPA.getBackBTS())


    # @unittest.skip("无条件跳过该测试")
    def test008_checkMainRankTotal(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkMainTotalRank())

    # @unittest.skip("无条件跳过该测试")
    def test009_checkMainRankNEW(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkMainNewRank())

    # @unittest.skip("无条件跳过该测试")
    def test010_checkMainRankWeek(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkMainWeekRank())

    # @unittest.skip("无条件跳过该测试")
    def test013_checkMainToRank(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInRankMore())
        self.assertTrue(self.DPA.getBackBTS())

    # @unittest.skip("无条件跳过该测试")
    def test014_checkMainDM(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkMainDMRecommendUI())

    # @unittest.skip("无条件跳过该测试")
    def test015_checkMainToDM(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInDMRecommendMore())
        self.assertTrue(self.DPA.getBackBTS())

    # @unittest.skip("无条件跳过该测试")
    def test016_checkMainPriority(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkMainPriorityUI())

    # @unittest.skip("无条件跳过该测试")
    def test017_checkMainToPriority(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInPriorityMore())
        self.assertTrue(self.DPA.getBack())

    # @unittest.skip("无条件跳过该测试")
    def test018_checkMainNew(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkMainNewTitleUI())

    # @unittest.skip("无条件跳过该测试")
    def test019_checkMainToNew(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInNewTitleMore())
        self.assertTrue(self.DPA.getBackBTS())

    # @unittest.skip("无条件跳过该测试")
    def test022_checkFirstBarBanner(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInBarBanner(0))

    # @unittest.skip("无条件跳过该测试")
    def test024_checkMainGenre(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkMainGenreUI())

    # @unittest.skip("无条件跳过该测试")
    def test025_checkMainToGenre(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInGenreMore())
        self.assertTrue(self.DPA.getBackBTS())

    # @unittest.skip("无条件跳过该测试")
    def test028_checkMainTheme(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkMainThemeUI())

    # @unittest.skip("无条件跳过该测试")
    def test029_checkMainToTheme(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInThemeMore())
        self.assertTrue(self.DPA.getBackBTS())

    # @unittest.skip("无条件跳过该测试")
    def test032_checkSecondBarBanner(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.getInBarBanner(1))

    # @unittest.skip("无条件跳过该测试")
    def test035_checkMenusHotwords(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkMenusPageHotword())

    # @unittest.skip("无条件跳过该测试")
    def test040_checkMenusPage(self):
        self.DPA.toDefaultPage("FOUND")
        self.assertTrue(self.DPA.getInDiscoveryXXPage())
        self.assertTrue(self.DPA.checkMenusPage())
