ALTER TABLE hideout.m_link_categories ADD COULMN m_user_id INT(3) NOT NULL COMMENT 'ユーザID';
ALTER TABLE hideout.m_link_categories ADD CONSTRAINT m_user_id FOREIGN KEY (m_user_id) REFERENCES m_users(m_user_id) ON DELETE CASCADE ON UPDATE CASCADE;

#ALTER TABLE hideout.m_links ADD COULMN m_user_id INT(3) NOT NULL COMMENT 'ユーザID';
ALTER TABLE hideout.m_links ADD CONSTRAINT m_user_id FOREIGN KEY (m_user_id) REFERENCES m_users(m_user_id) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS hideout.m_languages (
  m_language_id TINYINT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '言語ID',
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_language_name VARCHAR(50) NOT NULL COMMENT '名称'
) engine=InnoDB COMMENT='言語';
#ALTER TABLE hideout.m_languages ADD CONSTRAINT m_user_id FOREIGN KEY (m_user_id) REFERENCES m_users(m_user_id) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS hideout.t_words (
  t_word_id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '単語ID',
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_language_id TINYINT(2) NOT NULL COMMENT '言語ID',
  t_word_spell VARCHAR(50) NOT NULL COMMENT '綴り',
  t_word_explanation VARCHAR(1000) NOT NULL COMMENT '説明',
  t_word_pronunciation VARCHAR(50) NOT NULL DEFAULT '' COMMENT '発音',
  t_word_is_learned TINYINT(1) NOT NULL DEFAULT 0 COMMENT '習得済みフラグ 0: 未習得、1:習得済み',
  t_word_note VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '備考',
  t_word_created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '登録日'
) engine=InnoDB COMMENT='単語';

CREATE TABLE hideout.m_clients (
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_client_id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '取引先ID',
  m_client_name VARCHAR(100) NOT NULL COMMENT '取引先名称',
  m_client_document_prefix VARCHAR(4) NOT NULL COMMENT '帳票用接頭辞'
) engine=InnoDB COMMENT='取引先マスタ';

CREATE TABLE hideout.m_client_addresses (
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_client_address_id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '取引先住所ID',
  m_client_id INT(3) NOT NULL COMMENT '取引先ID',
  m_client_postal_code INT(7) NOT NULL COMMENT '郵便番号',
  m_client_prefecture INT(2) NOT NULL COMMENT '都道府県コード',
  m_client_city VARCHAR(200) NOT NULL COMMENT '市区町村',
  m_client_address VARCHAR(200) NOT NULL COMMENT '番地',
  m_client_building VARCHAR(200) NOT NULL COMMENT '建物名等'
) engine=InnoDB COMMENT='取引先住所マスタ';

CREATE TABLE hideout.m_client_personnels (
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_client_id INT(3) NOT NULL COMMENT '取引先ID',
  m_client_personnel_id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '取引先ID',
  m_client_personnel_name VARCHAR(100) NOT NULL COMMENT '取引先名称'
) engine=InnoDB COMMENT='取引先担当者マスタ';
