-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 06, 2022 at 01:13 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `user_name` text NOT NULL,
  `password` text NOT NULL,
  `mail` text NOT NULL,
  `mo_no` varchar(100) NOT NULL,
  `sdate` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`user_name`, `password`, `mail`, `mo_no`, `sdate`) VALUES
('niraj', 'bava', 'nirajbava222@gmail.com ', '9623828192', '2022-02-06 16:33:34');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `mono` varchar(12) NOT NULL,
  `message` text NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `mono`, `message`, `date`, `email`) VALUES
(1, 'niraj', '', 'bava', '2022-02-06 17:09:54', 'nirajbava333@gmail.c'),
(2, 'ghhgfh', '7587587587', 'xcxcxc', '2022-02-06 17:20:10', 'nirajbava222@gmail.c'),
(3, 'ghhgfh', '7587587587', 'xcxcxc', '2022-02-06 17:21:44', 'nirajbava222@gmail.c'),
(4, 'cc', '7587587587', 'ccxc', '2022-02-06 17:21:59', 'nirajbava222@gmail.c');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `title` text NOT NULL,
  `slug` text NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `image` text NOT NULL,
  `no` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`title`, `slug`, `content`, `date`, `image`, `no`) VALUES
('this niraj', 'niraj', 'this is post', '2022-02-06 16:34:23', '0', 1),
('this', 'this', 'this is post\r\n', '2022-02-06 16:57:47', 'logo2.png', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
