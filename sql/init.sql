CREATE DATABASE hideout;

CREATE TABLE IF NOT EXISTS hideout.m_users (
  m_user_id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'ユーザID',
  m_user_username VARCHAR(100) NOT NULL COMMENT 'ユーザ名称',
  m_user_hashed_password VARCHAR(256) NOT NULL COMMENT 'ハッシュ化済みパスワード'
) engine=InnoDB COMMENT='ユーザマスタ';

INSERT INTO hideout.m_users(m_user_id, m_user_username, m_user_hashed_password) VALUES ('1', 'admin', SHA2('admin', 256));

CREATE TABLE IF NOT EXISTS hideout.m_link_categories (
  m_link_category_id INT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'リンクカテゴリID',
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_link_category_name VARCHAR(100) NOT NULL COMMENT 'リンクカテゴリ名称',
  m_link_category_display_order INT(3) NOT NULL COMMENT 'リンクカテゴリ表示順序'
) engine=InnoDB COMMENT='リンクカテゴリマスタ';

ALTER TABLE hideout.m_link_categories ADD CONSTRAINT m_user_id FOREIGN KEY (m_user_id) REFERENCES m_users(m_user_id) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE IF NOT EXISTS hideout.m_links (
  m_link_id INT(4) NOT NULL COMMENT 'リンクID',
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_link_category_id INT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'リンクカテゴリID',
  m_link_site_name VARCHAR(100) NOT NULL COMMENT 'リンク名称',
  m_link_url VARCHAR(200) NOT NULL COMMENT 'リンク名URL',
  m_link_display_order INT(3) NOT NULL COMMENT 'リンク表示順序'
) engine=InnoDB COMMENT='リンクマスタ';

#ALTER TABLE hideout.m_links ADD CONSTRAINT m_user_id FOREIGN KEY (m_user_id) REFERENCES m_users(m_user_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE hideout.m_links ADD CONSTRAINT m_link_category_id FOREIGN KEY (m_link_category_id) REFERENCES m_link_categories(m_link_category_id) ON DELETE CASCADE ON UPDATE CASCADE;

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
  t_word_pronounciation VARCHAR(50) NOT NULL DEFAULT '' COMMENT '発音',
  t_word_is_learned TINYINT(1) NOT NULL DEFAULT 0 COMMENT '習得済みフラグ 0: 未習得、1:習得済み',
  t_word_note VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '備考',
  t_word_created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '登録日'
) engine=InnoDB COMMENT='単語';

CREATE TABLE IF NOT EXISTS hideout.m_account_titles (
  m_account_title_id INT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '勘定科目ID',
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_account_title_name VARCHAR(20) NOT NULL COMMENT '勘定科目',
  m_account_title_classification_type TINYINT(1) NOT NULL COMMENT '勘定科目分類区分 1: 資産, 2: 負債, 3: 資本, 4:費用, 5:収益'
) engine=InnoDB COMMENT='勘定科目';

CREATE TABLE IF NOT EXISTS hideout.t_journal_entries (
  m_journal_entry_id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '仕訳ID',
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_account_title_id INT(4) NOT NULL DEFAULT 0 COMMENT '勘定科目ID 0:未確定',
  m_journal_entry_transaction_date DATETIME NOT NULL COMMENT '取引日付',
  m_journal_entry_note VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '備考',
  m_journal_entry_created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '登録日'
) engine=InnoDB COMMENT='仕訳';
