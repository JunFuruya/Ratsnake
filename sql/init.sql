CREATE DATABASE hideout;

CREATE TABLE IF NOT EXISTS hideout.m_users (
  m_user_id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'ユーザID',
  m_user_username VARCHAR(100) NOT NULL COMMENT 'ユーザ名称',
  m_user_hashed_password VARCHAR(256) NOT NULL COMMENT 'ハッシュ化済みパスワード'
);

INSERT INTO hideout.m_users(m_user_id, m_user_username, m_user_hashed_password) VALUES ('1', 'admin', SHA2('admin', 256));

CREATE TABLE IF NOT EXISTS hideout.m_link_categories (
  m_link_category_id INT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'リンクカテゴリID',
  m_link_category_name VARCHAR(100) NOT NULL COMMENT 'リンクカテゴリ名称',
  m_link_category_display_order INT(3) NOT NULL COMMENT 'リンクカテゴリ表示順序'
);

CREATE TABLE IF NOT EXISTS hideout.m_links (
  m_link_id INT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'リンクID',
  m_link_site_name VARCHAR(100) NOT NULL COMMENT 'リンク名称',
  m_link_url VARCHAR(200) NOT NULL COMMENT 'リンク名URL',
  m_link_display_order INT(3) NOT NULL COMMENT 'リンク表示順序'
);

