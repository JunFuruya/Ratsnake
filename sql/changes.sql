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

CREATE TABLE IF NOT EXISTS hideout.m_account_titles (
  m_account_title_id INT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '勘定科目ID',
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_account_title_name VARCHAR(20) NOT NULL COMMENT '勘定科目',
  m_account_title_classification_type TINYINT(1) NOT NULL COMMENT '勘定科目分類区分 1: 資産, 2: 負債, 3: 資本, 4:費用, 5:収益'
) engine=InnoDB COMMENT='勘定科目';

CREATE TABLE IF NOT EXISTS hideout.t_journal_entries (
  t_journal_entry_id INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '仕訳ID',
  m_user_id INT(3) NOT NULL COMMENT 'ユーザID',
  m_account_title_id INT(4) NOT NULL DEFAULT 0 COMMENT '勘定科目ID 0:未確定',
  t_journal_entry_transaction_date DATETIME NOT NULL COMMENT '取引日付',
  t_journal_entry_note VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '備考',
  t_journal_entry_created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '登録日'
) engine=InnoDB COMMENT='仕訳';
