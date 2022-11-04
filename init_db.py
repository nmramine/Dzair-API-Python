import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

cur.execute("CREATE TABLE `Wilaya` (`code` int(11) NOT NULL, `name` varchar(1000) NOT NULL, `population` int(11) DEFAULT NULL, `surface` int(11) DEFAULT NULL)")

cur.execute("INSERT INTO `Wilaya` (`code`, `name`, `population`, `surface`) VALUES(1, 'Adrar', 439693, 427368),(2, 'Chlef', 1013718, 4791),(3, 'Laghouat', 477328, 25057),(4, 'Oum El Bouaghi', 644364, 7638),(5, 'Batna', 1128030, 12192),(6, 'Béjaïa', 915835, 3268),(7, 'Biskra', 730262, 20986),(8, 'Béchar', 274866, 162200),(9, 'Blida', 1009892, 1696),(10, 'Bouira', 695583, 4439),(11, 'Tamanrasset', 198691, 557906),(12, 'Tébessa', 657227, 14227),(13, 'Tlemcen', 949135, 9061),(14, 'Tiaret', 846823, 20673),(15, 'Tizi Ouzou', 1127608, 2993),(16, 'Alger', 2988145, 1190),(17, 'Djelfa', 1223223, 32256),(18, 'Jijel', 636948, 2399),(19, 'Sétif', 1496150, 6504),(20, 'Saïda', 330641, 6764),(21, 'Skikda', 904195, 4026),(22, 'Sidi Bel Abbès', 604744, 9151),(23, 'Annaba', 640050, 1439),(24, 'Guelma', 482430, 4101),(25, 'Constantine', 943112, 2197),(26, 'Médéa', 830943, 8866),(27, 'Mostaganem', 746947, 2269),(28, 'MSila', 991846, 18718),(29, 'Mascara', 784073, 5941),(30, 'Ouargla', 558558, 211980),(31, 'Oran', 1584607, 2114),(32, 'El Bayadh', 262187, 71697),(33, 'Illizi', 54490, 284618),(34, 'Bordj Bou Arreridj', 716423, 3920),(35, 'Boumerdès', 802083, 1456),(36, 'El Tarf', 411783, 3339),(37, 'Tindouf', 159898, 158874),(38, 'Tissemsilt', 296366, 3152),(39, 'El Oued', 673934, 54573),(40, 'Khenchela', 386683, 9715),(41, 'Souk Ahras', 440299, 4630),(42, 'Tipaza', 617661, 2166),(43, 'Mila', 768419, 3481),(44, 'Aïn Defla', 771890, 4897),(45, 'Naâma', 209470, 29514),(46, 'Aïn Témouchent', 384565, 2377),(47, 'Ghardaïa', 375988, 86105),(48, 'Relizane', 733060, 4870),(49, 'Timimoun', NULL, NULL),(50, 'Bordj Badji Mokhtar', NULL, NULL),(51, 'Ouled Djellal', NULL, NULL),(52, 'Béni Abbès', NULL, NULL),(53, 'In Salah', NULL, NULL),(54, 'In Guezzam', NULL, NULL),(55, 'Touggourt', NULL, NULL),(56, 'Djanet', NULL, NULL),(57, 'El MGhair', NULL, NULL),(58, 'El Meniaa', NULL, NULL);")

connection.commit()

connection.close()