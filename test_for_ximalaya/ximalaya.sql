/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : 127.0.0.1:3306
 Source Schema         : sz1905spider

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 25/10/2019 18:12:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ximalaya
-- ----------------------------
DROP TABLE IF EXISTS `ximalaya`;
CREATE TABLE `ximalaya`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `book_zhubo` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `book_href` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of ximalaya
-- ----------------------------
INSERT INTO `ximalaya` VALUES (16, '平凡的世界 | 路遥 著 (张震 杨晨倾情演绎,独家首发)', '新经典', 'https://www.ximalaya.com/youshengshu/22630007/p1');
INSERT INTO `ximalaya` VALUES (17, '小王子（经典必听）', '图特哈蒙', 'https://www.ximalaya.com/youshengshu/240506/p1');
INSERT INTO `ximalaya` VALUES (18, '武则天大全集（骆驼演播）', '读客熊猫君', 'https://www.ximalaya.com/youshengshu/20137641/p1');
INSERT INTO `ximalaya` VALUES (19, '离婚 老舍先生的中篇小说', '江涛声音工作室', 'https://www.ximalaya.com/youshengshu/10710983/p1');
INSERT INTO `ximalaya` VALUES (20, '解放战争名将粟裕珍闻录', '香港之声', 'https://www.ximalaya.com/youshengshu/13602341/p2');
INSERT INTO `ximalaya` VALUES (21, '骆驼祥子（原汁原味的品读）老舍', '董启言', 'https://www.ximalaya.com/youshengshu/15158548/p1');
