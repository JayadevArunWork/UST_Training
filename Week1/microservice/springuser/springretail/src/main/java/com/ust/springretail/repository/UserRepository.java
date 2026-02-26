package com.ust.springretail.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.ust.springretail.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
}