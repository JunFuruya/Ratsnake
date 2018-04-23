CREATE DATABASE hideout;

CREATE TABLE IF NOT EXISTS hideout.links (
  link_id INT(3) NOT NULL PRIMARY KEY COMMENT 'リンクID',
  link_site_name VARCHAR(100) NOT NULL COMMENT 'リンク名称',
  link_url VARCHAR(200) NOT NULL COMMENT 'リンク名URL',
  link_order  INT(3) NOT NULL COMMENT 'リンク名称'
);
