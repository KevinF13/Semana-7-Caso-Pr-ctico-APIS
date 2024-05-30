import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { CreateInventarioDto } from './dto/create-inventario.dto';
import { UpdateInventarioDto } from './dto/update-inventario.dto';
import { Inventario } from './Interface/inventario.interface';

@Injectable()
export class InventarioService {
  constructor(@InjectModel('Inventario') private readonly inventarioModel: Model<Inventario>) {}

  async create(createInventarioDto: CreateInventarioDto): Promise<Inventario> {
    const createdItem = new this.inventarioModel(createInventarioDto);
    return createdItem.save();
  }

  async findAll(): Promise<Inventario[]> {
    return this.inventarioModel.find().exec();
  }

  async findOne(id: string): Promise<Inventario> {
    return this.inventarioModel.findById(id).exec();
  }

  async update(id: string, updateInventarioDto: UpdateInventarioDto): Promise<Inventario> {
    return this.inventarioModel.findByIdAndUpdate(id, updateInventarioDto, { new: true }).exec();
  }

  async delete(id: string): Promise<Inventario> {
    return this.inventarioModel.findByIdAndDelete(id).exec(); // Cambio realizado aquí
  }
}
