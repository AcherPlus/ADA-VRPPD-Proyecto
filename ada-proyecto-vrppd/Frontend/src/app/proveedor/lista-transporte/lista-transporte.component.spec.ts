import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaTransporteComponent } from './lista-transporte.component';

describe('ListaTransporteComponent', () => {
  let component: ListaTransporteComponent;
  let fixture: ComponentFixture<ListaTransporteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListaTransporteComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ListaTransporteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
