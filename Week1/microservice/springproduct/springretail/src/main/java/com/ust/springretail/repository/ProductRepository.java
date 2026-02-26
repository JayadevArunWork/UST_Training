package com.ust.springretail.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.ust.springretail.entity.Product;

public interface ProductRepository extends JpaRepository<Product, Long> {
}